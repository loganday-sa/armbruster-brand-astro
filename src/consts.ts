// =============================================================================
// SITE CONFIGURATION
// =============================================================================

// Basic site info
export const SITE_TITLE = 'Scott Armbruster';
export const SITE_DESCRIPTION = 'AI Strategy & Systems at Every Level. Practical guides, case studies, and strategies for building AI-powered businesses.';
export const SITE_URL = 'https://armbruster-brand-astro.pages.dev';
export const SITE_AUTHOR = 'Scott Armbruster';

// Branding
export const SITE_LOGO = '/favicon.svg';
export const SITE_OG_IMAGE = '/images/og-default.png';

// Social links (leave empty string if not used)
export const SOCIAL_TWITTER = '@ScottArmbruster';
export const SOCIAL_LINKEDIN = 'https://www.linkedin.com/in/scottrarmbruster/';
export const SOCIAL_GITHUB = '';

// Newsletter/Email integration
export const NEWSLETTER_ACTION = '';
export const NEWSLETTER_METHOD = 'POST';

// Analytics (leave empty to disable)
export const GOOGLE_ANALYTICS_ID = '';
export const PLAUSIBLE_DOMAIN = '';

// =============================================================================
// CATEGORY CONFIGURATION
// =============================================================================

export interface CategoryConfig {
	name: string;
	path: string;
	icon: string;
	color: string;
	description: string;
}

export const CATEGORIES: Record<string, CategoryConfig> = {
	'AI Strategy': {
		name: 'AI Strategy',
		path: '/ai-strategy/',
		icon: '🎯',
		color: '#2563EB',
		description: 'Business strategy, ROI analysis, and AI adoption guidance',
	},
	'Implementation': {
		name: 'Implementation',
		path: '/implementation/',
		icon: '🔧',
		color: '#7C3AED',
		description: 'How-to guides, automation walkthroughs, and case studies',
	},
	'Industry': {
		name: 'Industry',
		path: '/industry/',
		icon: '📊',
		color: '#059669',
		description: 'AI news analysis, market trends, and industry shifts',
	},
	'Career': {
		name: 'Career',
		path: '/career/',
		icon: '🚀',
		color: '#D97706',
		description: 'Career positioning, side businesses, and professional growth',
	},
};

// Default category for posts without one
export const DEFAULT_CATEGORY = 'AI Strategy';

// Helper function to get category path from category name
export function getCategoryPath(category: string | undefined): string {
	if (!category || !CATEGORIES[category]) {
		return CATEGORIES[DEFAULT_CATEGORY].path;
	}
	return CATEGORIES[category].path;
}

// Helper function to get full category config
export function getCategoryConfig(category: string | undefined): CategoryConfig {
	if (!category || !CATEGORIES[category]) {
		return CATEGORIES[DEFAULT_CATEGORY];
	}
	return CATEGORIES[category];
}

// Get all category keys
export function getCategoryKeys(): string[] {
	return Object.keys(CATEGORIES);
}

// =============================================================================
// PAGINATION SETTINGS
// =============================================================================

export const POSTS_PER_PAGE = 12;

// =============================================================================
// CONTENT SETTINGS
// =============================================================================

// Number of related posts to show
export const RELATED_POSTS_COUNT = 3;

// Number of featured posts on homepage
export const FEATURED_POSTS_COUNT = 6;

// Reading time calculation (words per minute)
export const WORDS_PER_MINUTE = 200;

// Calculate reading time from content
export function getReadingTime(content: string | undefined): number {
	if (!content) return 1;
	const words = content.trim().split(/\s+/).length;
	return Math.ceil(words / WORDS_PER_MINUTE);
}
